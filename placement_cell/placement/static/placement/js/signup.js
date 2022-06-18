const usernameField=document.querySelector("#usernameField");
const emailField = document.querySelector("#emailField");
const usernameSuccessOutput= document.querySelector(".usernameSuccessOutput")
const emailSuccessOutput = document.querySelector(".emailSuccessOutput")
const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#passwordField');
const sumbitbtn= document.querySelector('#signupDetail')



  
togglePassword.addEventListener('click', function (e) {
         console.log("enterd eye funtion")
          if($(this).hasClass('fa-eye-slash')){
             
            $(this).removeClass('fa-eye-slash');
            
            $(this).addClass('fa-eye');
            
            $('#passwordField').attr('type','text');
              
          }else{
           
            $(this).removeClass('fa-eye');
            
            $(this).addClass('fa-eye-slash');  
            
            $('#passwordField').attr('type','password');
          }
      });

emailField.addEventListener("keyup", (e) =>{
    console.log("enter emailfieled")
    const emailVal = e.target.value;
    
    
    if(emailVal.length>0){
        emailSuccessOutput.style.display="block"
        emailSuccessOutput.textContent = `valid email`
    }
    else{
        sumbitbtn.removeAttribute("disabled");


        emailSuccessOutput.style.display="none"
    }
    
    
    console.log("email",emailVal)
    emailField.classList.remove("fm-inavlid")
    emailField.classList.add("fm-valid")
    $('.email_error').hide();
    if (emailVal.length > 0) {
        fetch("signup", {
          body: JSON.stringify({ email: emailVal }),
          method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
        console.log("data", data);
        if (data.email_error) {
            sumbitbtn.disabled = true;
            emailSuccessOutput.style.display="none"
            console.log("enter emailfielederror")
            emailField.classList.remove("fm-valid")
            emailField.classList.add("fm-inavlid")
            $('.email_error').show();
            $(`.email_error`).html(`<ul class="errorlist"><li>${data.email_error}</li></ul>`);
        }else{
            sumbitbtn.removeAttribute("disabled");
        }
    });
     }
    });
usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
    if (usernameVal.length > 0){
        usernameSuccessOutput.style.display="block"
        usernameSuccessOutput.textContent = `valid username`
    }
    else{
        sumbitbtn.removeAttribute("disabled");
        usernameSuccessOutput.style.display="none"
    }
    console.log("user",usernameVal)
    usernameField.classList.remove("fm-inavlid")
    usernameField.classList.add("fm-valid")
    $('.image_error').hide();
    if (usernameVal.length > 0)
    {  
    fetch("signup", { 
        body: JSON.stringify({ username: usernameVal }),
        method:"POST",
     })
    .then((res) => res.json())
    .then((data) => {
        console.log("data",data)
       
        if(data.username_error){
            sumbitbtn.disabled = true;
            usernameSuccessOutput.style.display="none"
            usernameField.classList.remove("fm-valid")
            usernameField.classList.add("fm-inavlid")
            $('.image_error').show();
            $(`.image_error`).html(`<ul class="errorlist"><li>${data.username_error}</li></ul>`);
        }else{
            sumbitbtn.removeAttribute("disabled");
        }
    });
     }
    });