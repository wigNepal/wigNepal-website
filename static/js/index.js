

// function registration_success_msg(){
//     alert("We are launching soon. Thank you for visiting.");
// }
// clicking the register button
function toggleForm() {
    window.open('regform', '_blank');
}


// function toggleForm() {
//     var form = document.getElementById('register-form');
//     if (form.style.display === 'none') {
//         form.style.display = 'block';
//     } else {
//         form.style.display = 'none';
//     }
// }

// regBtn.addEventListener('mouseover',function(){
//     regBtn.classList.add('btn--primary-hover');
// });
// regBtn.addEventListener('mouseout',function(){
//     regBtn.classList.remove('btn--primary-hover');
// });

// const regBtn2 = document.getElementById("btnRegistration2");
// function registration_success_msg(){
//     alert("We are launching soon. Thank you for visiting.");
// }
// // clicking the register button
// regBtn2.addEventListener('click',registration_success_msg);

// regBtn2.addEventListener('mouseover',function(){
//     regBtn2.classList.add('btn--primary-hover');
// });
// regBtn2.addEventListener('mouseout',function(){
//     regBtn2.classList.remove('btn--primary-hover');
// });

// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('btnRegistration').addEventListener('click', function() {
//         var form = document.getElementById('btnRegistration');
//         var formData = new FormData(form);

//         fetch(form.action, {
//             method: 'POST',
//             headers: {
//                 'X-CSRFToken': '{{ csrf_token }}'
//             },
//             body: formData
//         })
//         .then(response => {
//             if (response.ok) {
//                 // Optionally handle success response
//                 alert('Form submitted successfully!');
//             } else {
//                 // Optionally handle error response
//                 alert('Form submission failed!');
//             }
//         })
//         .catch(error => {
//             // Handle network errors or other exceptions
//             console.error('Error:', error);
//             alert('Form submission failed!');
//         });
//     });
// });
