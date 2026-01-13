document.addEventListener("DOMContentLoaded", function () {
    console.log("Flask Blog loaded successfully");

    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = "none";
        }, 3000);
    });
});
