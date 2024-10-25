document.getElementById("downloadButton").addEventListener("click", function(event) {
    event.preventDefault(); // Prevenir la navegación por defecto

    fetch("/dataset/download_all")
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.style.display = "none";
            a.href = url;
            a.download = "all_datasets.zip";
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error("Error downloading the file:", error));
});