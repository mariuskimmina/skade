window.onload = function() {
  $("#skadeDropzone").dropzone({
    url: 'upload',
    paramName: "file",
    maxFilesize: 500000,
    timeout: 0,
    autoProcessQueue: false,
    uploadMultiple: true,
    createImageThumbnails: false,
  })
  //Dropzone.options.skadeDropzone = {
   // url: 'upload',
    //paramName: "file",
    //maxFilesize: 500000,
    //timeout: 0,
    //autoProcessQueue: false,
    //uploadMultiple: true,
    //createImageThumbnails: false,
    //init: function() {
      //dzClosure = this; // Makes sure that 'this' is understood inside the functions below.

      // for Dropzone to process the queue (instead of default form behavior):
      //document.getElementById("submit-all").addEventListener("click", function(e) {
          // Make sure that the form isn't actually being sent.
          //e.preventDefault();
          //e.stopPropagation();
          //dzClosure.processQueue();
      //});

      //send all the form data along with the files:
      //this.on("sendingmultiple", function(data, xhr, formData) {
          //formData.append("firstname", jQuery("#firstname").val());
          //formData.append("lastname", jQuery("#lastname").val());
      //});
    //}
  //}   
}