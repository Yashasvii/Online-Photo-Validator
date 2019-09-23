    var filePath = "";
    var type = ""


        $(document).ready(function () {

            $("#uploadFolder").click(function (event) {

                //stop submit the form, we will post it manually.
                event.preventDefault();

                $("#uploadFolder").prop("disabled", true);

                // Get form
                var form = $('#fileUploadForm')[0];

                // Create an FormData object
                var data = new FormData(form);

                data.append("info", "");

                var selectedValue =  $('#categoryDropDown').find("option:selected").val();

                 if(selectedValue === "folder"){
                    data.append("type","folder");
                    type="folder"
                }

                 else{
                     data.append("type","file");
                     type="file"
                 }
                $.ajax({
                    type: "POST",
                    enctype: 'multipart/form-data',
                    url: "/dialogueBox/",
                    data: data,
                    processData: false,
                    contentType: false,
                    cache: false,
                    timeout: 600000,
                    success: function (data) {

                        filePath = data;
                          $("#uploadFolder").prop("disabled", false);
                              $("#btnSubmit").prop("disabled", false);
                        $("#selectedFolderText").html(data + "/").wrap('<pre />');;
                    },
                    error: function (e) {
                          $("#uploadFolder").prop("disabled", false);
                    }
                });

            });

            $("#btnSubmit").click(function (event) {
                $("#result").html("Processing..").wrap('<pre />');

                //stop submit the form, we will post it manually.
                event.preventDefault();

                // Get form
                var form = $('#fileUploadForm')[0];

                // Create an FormData object
                var data = new FormData(form);


                data.append("path", filePath);


                data.append("type", type);

                // If you want to add an extra field for the FormData
                //data.append("CustomField", "This is some extra data, testing");

                // disabled the submit button

                $("#btnSubmit").prop("disabled", true);

                $.ajax({
                    type: "POST",
                    enctype: 'multipart/form-data',
                    url: "/upload/",
                    data: data,
                    processData: false,
                    contentType: false,
                    cache: false,
                    timeout: 600000,
                    success: function (data) {

                        if(type === "file")
                             $("#result").css("font-size","small");

                        $("#result").html(data).wrap('<pre />');;
                        console.log("SUCCESS : ", data);
                        $("#btnSubmit").prop("disabled", false);

                    },
                    error: function (e) {

                        // {#$("#result").text(e.responseText);#}
                        // {#console.log("ERROR : ", e);#}
                        // {#$("#btnSubmit").prop("disabled", false);#}

                    }
                });

            });

//             $('#SpaceAccommodation').change(function () {
//     var selectedText = $(this).find("option:selected").text();
//
//     $("").text(selectedText);
// });


        });