
function sendMail(contactForm) {
    emailjs.send("gmail", "wildlife", {
        "from_email": contactForm.email.value,
        "form_used": contactForm.textarea1.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}