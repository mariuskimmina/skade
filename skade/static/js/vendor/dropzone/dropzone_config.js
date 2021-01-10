window.onload = function() {
  $("#skadeDropzone").dropzone({
    url: 'upload',
    paramName: "file",
    maxFilesize: 500000,
    timeout: 0,
    autoProcessQueue: false,
    uploadMultiple: true,
    parallelUploads: 100,
    maxFiles: 100,
    createImageThumbnails: false,
    init: function() {
        dzClosure = this; // Makes sure that 'this' is understood inside the functions below.

        // for Dropzone to process the queue (instead of default form behavior):
        document.getElementById("submit-all").addEventListener("click", function(e) {
            console.log("YES")
            // Make sure that the form isn't actually being sent.
            e.preventDefault();
            e.stopPropagation();
            dzClosure.processQueue();
        });

        //send all the form data along with the files:
        this.on("sendingmultiple", function(data, xhr, formData) {
            formData.append("yarascan", jQuery("#yarascan").val());
        });
    }
  })
}