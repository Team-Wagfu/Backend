const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// Canvas center coordinates
const centerX = canvas.width / 2;
const centerY = canvas.height / 2; // Adjust for full height

// Radius of the semicircle
const radius = 100; // Change this for larger/smaller semicircle

// Start and end angles for the right half
const startAngle = - Math.PI / 2; // Start at the top
const endAngle = Math.PI / 2; // End at the bottom

// Draw filled semicircle
ctx.beginPath();
ctx.arc(centerX, centerY, radius, startAngle, endAngle, false);
ctx.lineTo(centerX, centerY); // Draw line back to center
ctx.fillStyle = 'orange'; // Change color as needed
ctx.fill();
ctx.strokeStyle = 'black'; // Outline color
ctx.lineWidth = 5; // Outline width
ctx.stroke();
