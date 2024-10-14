const canvas = document.getElementById('snow-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

let snowflakes = [];

function createSnowflakes() {
    snowflakes = [];
    for (let i = 0; i < 100; i++) {
        snowflakes.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            opacity: Math.random(),
            speedX: Math.random() * 1 - 0.5,
            speedY: Math.random() * 3 + 1,
            radius: Math.random() * 3 + 1
        });
    }
}

function drawSnowflakes() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'white';
    ctx.beginPath();
    for (let i = 0; i < snowflakes.length; i++) {
        const sf = snowflakes[i];
        ctx.moveTo(sf.x, sf.y);
        ctx.arc(sf.x, sf.y, sf.radius, 0, Math.PI * 2, true);
    }
    ctx.fill();
    moveSnowflakes();
}

function moveSnowflakes() {
    for (let i = 0; i < snowflakes.length; i++) {
        const sf = snowflakes[i];
        sf.x += sf.speedX;
        sf.y += sf.speedY;

        if (sf.y > canvas.height) {
            sf.y = 0;
            sf.x = Math.random() * canvas.width;
        }

        if (sf.x > canvas.width) {
            sf.x = 0;
        } else if (sf.x < 0) {
            sf.x = canvas.width;
        }
    }
}

function animateSnow() {
    drawSnowflakes();
    requestAnimationFrame(animateSnow);
}

createSnowflakes();
animateSnow();
