// Physiological State Chart
const ctx1 = document.getElementById('physioChart').getContext('2d');
const physioChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Physiological State',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Brainwave Patterns Chart
const ctx2 = document.getElementById('brainwaveChart').getContext('2d');
const brainwaveChart = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [{
            label: 'Brainwave Patterns',
            data: [120, 110, 130, 140],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Activity Chart
const ctx3 = document.getElementById('activityChart').getContext('2d');
const activityChart = new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: ['Yoga', 'Meditation', 'Other'],
        datasets: [{
            label: 'Activity Levels',
            data: [50, 25, 25],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    }
});

// Meditation Chart
const ctx4 = document.getElementById('meditationChart').getContext('2d');
const meditationChart = new Chart(ctx4, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Meditation Excellence',
            data: [4.5, 4.7, 4.6, 4.8, 5.0, 4.9, 4.8],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Function to display saved results from localStorage on dashboard load
document.addEventListener('DOMContentLoaded', function () {
    // Display Pregnancy Weight Gain Result
    const weightGainResult = localStorage.getItem('weightGainResult');
    if (weightGainResult) {
        document.getElementById('displayWeightGainResult').innerText = weightGainResult;
    }

    // Display Ovulation Date Result
    const ovulationResult = localStorage.getItem('ovulationResult');
    if (ovulationResult) {
        document.getElementById('displayOvulationResult').innerText = ovulationResult;
    }
});

// Pregnancy Weight Gain Calculator
function calculateWeightGain() {
    const prePregnancyWeight = parseFloat(document.getElementById('prePregnancyWeight').value);
    const currentWeek = parseInt(document.getElementById('currentWeek').value);
    const height = parseInt(document.getElementById('height').value);

    if (!prePregnancyWeight || !currentWeek || !height) {
        alert('Please fill in all fields.');
        return;
    }

    // Calculate BMI
    const heightInMeters = height / 100;
    const bmi = prePregnancyWeight / (heightInMeters * heightInMeters);

    // Calculate recommended weight gain based on BMI
    let recommendedWeightGain;
    if (bmi < 18.5) {
        recommendedWeightGain = '13 to 18 kg';
    } else if (bmi >= 18.5 && bmi < 24.9) {
        recommendedWeightGain = '11 to 16 kg';
    } else if (bmi >= 25 && bmi < 29.9) {
        recommendedWeightGain = '7 to 11 kg';
    } else {
        recommendedWeightGain = '5 to 9 kg';
    }

    const weightGainMessage = `Recommended weight gain: ${recommendedWeightGain} based on your BMI of ${bmi.toFixed(1)}.`;
    
    // Display the result
    document.getElementById('weightGainResult').innerText = weightGainMessage;

    // Save result to localStorage
    localStorage.setItem('weightGainResult', weightGainMessage);
}

// Ovulation Calculator
function calculateOvulation() {
    const lastPeriod = new Date(document.getElementById('lastPeriod').value);
    const cycleLength = parseInt(document.getElementById('cycleLength').value);

    if (!lastPeriod || !cycleLength) {
        alert('Please fill in all fields.');
        return;
    }

    // Calculate ovulation day (usually 14 days before the next period)
    const ovulationDay = new Date(lastPeriod);
    ovulationDay.setDate(lastPeriod.getDate() + cycleLength - 14);

    // Display result
    const formattedOvulationDay = ovulationDay.toLocaleDateString();
    const ovulationMessage = `Your next ovulation date is around: ${formattedOvulationDay}`;

    // Display the result
    document.getElementById('ovulationResult').innerText = ovulationMessage;

    // Save result to localStorage
    localStorage.setItem('ovulationResult', ovulationMessage);
}

