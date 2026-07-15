/* ==========================================================================
   EDU PREDICT FRONTEND LOGIC (JS)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // Current application state
    let statsData = null;
    let attendanceChart = null;
    let studyHoursChart = null;
    let distributionChart = null;

    // Toast Notifications helper
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');
    
    function showToast(message, type = 'info') {
        toastMessage.textContent = message;
        toast.className = 'toast-notification show ' + type;
        
        // Change icon based on type
        const icon = toast.querySelector('.toast-icon');
        icon.className = 'fa-solid toast-icon';
        if (type === 'success') icon.classList.add('fa-circle-check');
        else if (type === 'error') icon.classList.add('fa-circle-exclamation');
        else if (type === 'warning') icon.classList.add('fa-triangle-exclamation');
        else icon.classList.add('fa-circle-info');

        setTimeout(() => {
            toast.classList.remove('show');
        }, 3500);
    }

    // ==========================================================================
    // 1. Sidebar Navigation / Tab Switching
    // ==========================================================================
    const navItems = document.querySelectorAll('.nav-item');
    const tabContents = document.querySelectorAll('.tab-content');
    const pageTitle = document.getElementById('page-title');
    const pageSubtitle = document.getElementById('page-subtitle');

    const tabMeta = {
        'dashboard': {
            title: 'Dashboard Overview',
            subtitle: 'Insights and analysis of the active student performance dataset.'
        },
        'single-predict': {
            title: 'Predict Student Grade',
            subtitle: 'Input a student\'s hours, attendance, and midterm score to run regression.'
        },
        'model-details': {
            title: 'Cleaned Training Dataset',
            subtitle: 'Showing records loaded from data/student_performance_cleaned.csv'
        }
    };

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');
            
            // Toggle active menu class
            navItems.forEach(n => n.classList.remove('active'));
            item.classList.add('active');
            
            // Toggle active tab content
            tabContents.forEach(content => {
                content.classList.remove('active');
                if (content.id === targetTab) {
                    content.classList.add('active');
                }
            });

            // Update Headers
            if (tabMeta[targetTab]) {
                pageTitle.textContent = tabMeta[targetTab].title;
                pageSubtitle.textContent = tabMeta[targetTab].subtitle;
            }

            // Lazy resize charts if switching to dashboard
            if (targetTab === 'dashboard') {
                setTimeout(resizeCharts, 50);
            }
        });
    });

    function resizeCharts() {
        if (attendanceChart) attendanceChart.resize();
        if (studyHoursChart) studyHoursChart.resize();
        if (distributionChart) distributionChart.resize();
    }

    // ==========================================================================
    // 2. Interactive Input Sliders (Single Prediction View)
    // ==========================================================================
    const sliders = [
        { id: 'attendance', displayId: 'attendanceVal', suffix: '%' },
        { id: 'study_hours', displayId: 'studyHoursVal', suffix: ' hrs' },
        { id: 'midterm_marks', displayId: 'midtermVal', suffix: ' / 100' }
    ];

    sliders.forEach(sliderInfo => {
        const slider = document.getElementById(sliderInfo.id);
        const display = document.getElementById(sliderInfo.displayId);
        
        if (slider && display) {
            slider.addEventListener('input', (e) => {
                display.textContent = e.target.value + sliderInfo.suffix;
            });
        }
    });

    // ==========================================================================
    // 3. API - Single Prediction Form Handler
    // ==========================================================================
    const predictionForm = document.getElementById('predictionForm');
    const resultPanel = document.getElementById('resultPanel');
    const resultPlaceholder = document.getElementById('resultPlaceholder');
    const resultContent = document.getElementById('resultContent');

    predictionForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const studentName = document.getElementById('student_name').value.trim();
        const attendance = parseFloat(document.getElementById('attendance').value);
        const study_hours = parseFloat(document.getElementById('study_hours').value);
        const midterm_marks = parseFloat(document.getElementById('midterm_marks').value);

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ attendance, study_hours, midterm_marks })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Prediction failed');
            }

            const data = await response.json();
            displayPredictionResults(studentName, data, attendance, study_hours, midterm_marks);
            showToast('Prediction generated successfully!', 'success');
        } catch (error) {
            console.error('Prediction Error:', error);
            showToast(error.message, 'error');
        }
    });

    function displayPredictionResults(name, result, attendance, studyHours, midterm) {
        // Toggle panel states
        resultPanel.classList.remove('placeholder-state');
        resultPlaceholder.classList.add('hidden');
        resultContent.classList.remove('hidden');

        // Student Name Heading
        const nameHeading = document.getElementById('studentDisplayName');
        nameHeading.textContent = name ? `${name}'s Grade Analysis` : 'Student Performance Analysis';

        // Score display
        const score = result.prediction.toFixed(1);
        document.getElementById('predictedScore').textContent = score;

        // Circular Gauge Animation
        const gaugeFill = document.getElementById('gaugeProgress');
        const r = gaugeFill.r.baseVal.value;
        const circum = 2 * Math.PI * r; // 471.24
        
        // Calculate offset (percentage of circum)
        const offset = circum - (circum * result.prediction / 100);
        gaugeFill.style.strokeDashoffset = offset;

        // Status Badge Style mapping
        const badge = document.getElementById('riskBadge');
        badge.textContent = result.category;
        badge.className = 'badge'; // Reset

        if (result.category === 'Excellent') {
            badge.classList.add('excellent');
            gaugeFill.style.stroke = '#10b981';
        } else if (result.category === 'Good') {
            badge.classList.add('good');
            gaugeFill.style.stroke = '#0ea5e9';
        } else if (result.category === 'Average') {
            badge.classList.add('average');
            gaugeFill.style.stroke = '#f59e0b';
        } else {
            badge.classList.add('at-risk');
            gaugeFill.style.stroke = '#ef4444';
        }

        // Recommendations Text
        document.querySelector('#attendanceAdvice .advice-text').innerHTML = `<strong>Attendance (${attendance}%):</strong> ${result.recommendations.attendance}`;
        document.querySelector('#studyAdvice .advice-text').innerHTML = `<strong>Study Routine (${studyHours} hrs):</strong> ${result.recommendations.study_hours}`;
        document.querySelector('#midtermAdvice .advice-text').innerHTML = `<strong>Midterm Exam (${midterm}/100):</strong> ${result.recommendations.midterm_marks}`;
        
        // Overall Action alert
        const summaryAlert = document.getElementById('overallSummary');
        summaryAlert.textContent = result.recommendations.overall;
        summaryAlert.className = 'advice-alert'; // Reset
        
        if (result.category === 'Excellent' || result.category === 'Good') {
            summaryAlert.classList.add('normal');
        } else if (result.category === 'Average') {
            summaryAlert.classList.add('caution');
        } else {
            summaryAlert.classList.add('danger');
        }
    }

    // ==========================================================================
    // 4. API - Load Dataset, Correlation and Model stats
    // ==========================================================================
    async function loadDashboardStats() {
        try {
            const response = await fetch('/api/stats');
            if (!response.ok) throw new Error('Could not fetch dataset stats.');
            
            statsData = await response.json();
            
            // Populate metrics summary
            document.getElementById('stat-r2').textContent = (statsData.metrics.r2 * 100).toFixed(1) + '%';
            document.getElementById('stat-attendance').textContent = statsData.averages.Attendance.toFixed(1) + '%';
            document.getElementById('stat-hours').textContent = statsData.averages.StudyHours.toFixed(1) + ' hrs';
            document.getElementById('stat-midterm').textContent = statsData.averages.MidtermMarks.toFixed(1) + '/100';



            // Populate Cleaned Dataset Table
            renderDatasetTable(statsData.dataset);

            // Generate Heatmap grid
            renderCorrelationHeatmap(statsData.correlation);

            // Build/Update Charts
            initCharts(statsData.dataset);

        } catch (error) {
            console.error('Stats loading error:', error);
            showToast('Error loading dataset statistics. Check server console.', 'error');
        }
    }

    function renderDatasetTable(records) {
        const tbody = document.querySelector('#datasetTable tbody');
        tbody.innerHTML = '';
        
        records.forEach((row, idx) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>#${idx + 1}</strong></td>
                <td>${row.Attendance}%</td>
                <td>${row.StudyHours} hrs</td>
                <td>${row.MidtermMarks}</td>
                <td><strong>${row.FinalMarks}</strong></td>
            `;
            tbody.appendChild(tr);
        });
    }

    function renderCorrelationHeatmap(corrMatrix) {
        const grid = document.getElementById('heatmapGrid');
        grid.innerHTML = '';

        const vars = ['Attendance', 'StudyHours', 'MidtermMarks', 'FinalMarks'];
        
        // We will make a 5x5 grid. Top row and left column will be headers.
        // CSS grid defined as 4 columns, but we will inject elements appropriately.
        // Wait, index.html heatmap-grid has 4x4 layout: grid-template-columns: repeat(4, 75px)
        // Let's inspect the layout. We have 4 columns, 4 rows.
        // Let's render the correlation variables directly inside it.
        // The correlation matrix is a 4x4 of the numerical keys.
        
        vars.forEach((v1, rIdx) => {
            vars.forEach((v2, cIdx) => {
                const score = corrMatrix[v1][v2];
                const cell = document.createElement('div');
                cell.className = 'heatmap-cell';
                
                // Color scaling based on value
                // Positive correlation -> Indigo tint
                // Negative correlation -> Rose tint
                let bgColor = 'rgba(241, 245, 249, 1)'; // Neutral
                let textColor = '#0f172a';
                
                if (score > 0.01) {
                    bgColor = `rgba(79, 70, 229, ${score * 0.95})`; // primary indigo opacity
                    textColor = score > 0.55 ? '#ffffff' : '#0f172a';
                } else if (score < -0.01) {
                    bgColor = `rgba(239, 68, 68, ${Math.abs(score) * 0.95})`; // primary danger rose opacity
                    textColor = Math.abs(score) > 0.55 ? '#ffffff' : '#0f172a';
                }
                
                cell.style.backgroundColor = bgColor;
                cell.style.color = textColor;
                cell.innerHTML = `
                    <span style="font-weight:700;font-size:0.8rem;">${score.toFixed(2)}</span>
                    <span style="font-size:0.55rem;opacity:0.85;text-transform:uppercase;">${v1.substring(0,3)} vs ${v2.substring(0,3)}</span>
                `;
                
                // Set tooltip description
                cell.title = `Correlation between ${v1} and ${v2}: ${score.toFixed(4)}`;
                grid.appendChild(cell);
            });
        });
    }

    // ==========================================================================
    // 5. Chart.js Implementation
    // ==========================================================================
    function initCharts(records) {
        // Destroy existing instances if refreshing
        if (attendanceChart) attendanceChart.destroy();
        if (studyHoursChart) studyHoursChart.destroy();
        if (distributionChart) distributionChart.destroy();

        const finalMarks = records.map(r => r.FinalMarks);
        const attendances = records.map(r => r.Attendance);
        const studyHoursList = records.map(r => r.StudyHours);
        
        // 1. Attendance vs Final Marks (Scatter Plot)
        const ctxAtt = document.getElementById('attendanceChart').getContext('2d');
        const attScatterData = records.map(r => ({ x: r.Attendance, y: r.FinalMarks }));
        attendanceChart = new Chart(ctxAtt, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Students',
                    data: attScatterData,
                    backgroundColor: 'rgba(79, 70, 229, 0.65)',
                    borderColor: 'rgba(79, 70, 229, 1)',
                    borderWidth: 1,
                    pointRadius: 6,
                    pointHoverRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Attendance (%)', color: '#475569', font: { weight: 600 } },
                        grid: { color: '#f1f5f9' }
                    },
                    y: {
                        title: { display: true, text: 'Final Marks', color: '#475569', font: { weight: 600 } },
                        grid: { color: '#f1f5f9' },
                        min: 40,
                        max: 100
                    }
                }
            }
        });

        // 2. Study Hours vs Final Marks (Scatter Plot)
        const ctxHours = document.getElementById('studyHoursChart').getContext('2d');
        const hoursScatterData = records.map(r => ({ x: r.StudyHours, y: r.FinalMarks }));
        studyHoursChart = new Chart(ctxHours, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Students',
                    data: hoursScatterData,
                    backgroundColor: 'rgba(14, 165, 233, 0.65)',
                    borderColor: 'rgba(14, 165, 233, 1)',
                    borderWidth: 1,
                    pointRadius: 6,
                    pointHoverRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Study Hours / Week', color: '#475569', font: { weight: 600 } },
                        grid: { color: '#f1f5f9' }
                    },
                    y: {
                        title: { display: true, text: 'Final Marks', color: '#475569', font: { weight: 600 } },
                        grid: { color: '#f1f5f9' },
                        min: 40,
                        max: 100
                    }
                }
            }
        });

        // 3. Final Marks Distribution (Histogram)
        // Group final marks into bins: <60, 60-69, 70-79, 80-89, 90+
        const bins = { '<60': 0, '60-69': 0, '70-79': 0, '80-89': 0, '90+': 0 };
        finalMarks.forEach(mark => {
            if (mark < 60) bins['<60']++;
            else if (mark < 70) bins['60-69']++;
            else if (mark < 80) bins['70-79']++;
            else if (mark < 90) bins['80-89']++;
            else bins['90+']++;
        });

        const ctxDist = document.getElementById('distributionChart').getContext('2d');
        distributionChart = new Chart(ctxDist, {
            type: 'bar',
            data: {
                labels: Object.keys(bins),
                datasets: [{
                    data: Object.values(bins),
                    backgroundColor: [
                        'rgba(239, 68, 68, 0.75)',   // At Risk (Red)
                        'rgba(245, 158, 11, 0.75)',  // Average (Amber)
                        'rgba(59, 130, 246, 0.75)',  // Satisfactory (Blue)
                        'rgba(14, 165, 233, 0.75)',  // Good (Cyan)
                        'rgba(16, 185, 129, 0.75)'   // Excellent (Green)
                    ],
                    borderRadius: 6,
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Marks Grade Range', color: '#475569', font: { weight: 600 } },
                        grid: { display: false }
                    },
                    y: {
                        title: { display: true, text: 'Number of Students', color: '#475569', font: { weight: 600 } },
                        grid: { color: '#f1f5f9' },
                        ticks: { stepSize: 1 }
                    }
                }
            }
        });
    }


    // ==========================================================================
    // Initializer
    // ==========================================================================
    loadDashboardStats();
});
