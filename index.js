
const regBtn = document.getElementById("btnRegistration");
function registration_success_msg(){
    alert("We are launching soon. Thank you for visiting.");
}
// clicking the register button
regBtn.addEventListener('click',registration_success_msg);

regBtn.addEventListener('mouseover',function(){
    regBtn.classList.add('btn--primary-hover');
});
regBtn.addEventListener('mouseout',function(){
    regBtn.classList.remove('btn--primary-hover');
});

