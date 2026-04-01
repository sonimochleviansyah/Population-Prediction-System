console.log("ready");
// efek masuk halus
document.body.style.opacity = 0;

window.onload = () => {
    document.body.style.transition = "1s";
    document.body.style.opacity = 1;
};

// efek klik tombol
const btn = document.querySelector("button");

if (btn) {
    btn.addEventListener("click", () => {
        btn.innerText = "Processing...";
    });
}