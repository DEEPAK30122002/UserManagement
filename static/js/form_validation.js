document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const emailField = document.querySelector("#id_email");
  const phoneField = document.querySelector("#id_phone_number");

  form.addEventListener("submit", (event) => {
    if (!validateEmail(emailField.value) || !validatePhone(phoneField.value)) {
      event.preventDefault(); // Stop form submission if invalid
      alert("Please correct the errors before submitting.");
    }
  });

  // Validate Email
  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!re.test(email)) {
      emailField.setCustomValidity("Invalid email format");
      return false;
    }
    emailField.setCustomValidity("");
    return true;
  }

  // Validate Phone Number (digits only, 10-15 digits)
  function validatePhone(phone) {
    const re = /^\d{10,15}$/;
    if (!re.test(phone)) {
      phoneField.setCustomValidity("Phone number must be 10 to 15 digits.");
      return false;
    }
    phoneField.setCustomValidity("");
    return true;
  }
});
