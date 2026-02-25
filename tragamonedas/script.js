function spin() {
    const symbols = ["🍒", "🍋", "🍊", "🍇", "⭐", "💎"];
    const reel1 = symbols[Math.floor(Math.random() * symbols.length)];
    const reel2 = symbols[Math.floor(Math.random() * symbols.length)];
    const reel3 = symbols[Math.floor(Math.random() * symbols.length)];

    document.getElementById("reel1").textContent = reel1;
    document.getElementById("reel2").textContent = reel2;
    document.getElementById("reel3").textContent = reel3;

    if (reel1 === reel2 && reel2 === reel3) {
        document.getElementById("result").textContent = "🎉 ¡Ganaste!";
    } else {
        document.getElementById("result").textContent = "😢 Intenta de nuevo";
    }
}
