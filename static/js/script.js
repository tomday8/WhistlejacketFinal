const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let iterations = 0;

function shuffleTitle() {
    const interval = setInterval(() => {
        document.getElementById("titlepage").innerText = document.getElementById("titlepage").innerText.split("")
            .map((letter, index) => {
                if (index < iterations){
                    return document.getElementById("titlepage").dataset.value[index];
                }
                return letters[Math.floor(Math.random() * 26)]
            })
            .join("");

        if(iterations >= document.getElementById("titlepage").dataset.value.length) clearInterval(interval);
        iterations += 1;

    }, 40);
}

shuffleTitle();