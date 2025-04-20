document.addEventListener("DOMContentLoaded", () => {
    const sidebarToggleBtn = document.querySelector(".hamburger-btn");
    const sidebar = document.getElementById("sidebar");
    const appWrapper = document.querySelector(".app-wrapper");
  
    sidebarToggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("active");
      appWrapper.classList.toggle("sidebar-open");
    });
  
    const userIconBtn = document.getElementById("userIconBtn");
    const userDropdown = document.getElementById("userDropdown");
  
    userIconBtn.addEventListener("click", () => {
      userDropdown.style.display =
        userDropdown.style.display === "flex" ? "none" : "flex";
    });
  
    document.addEventListener("click", (e) => {
      if (!userIconBtn.contains(e.target) && !userDropdown.contains(e.target)) {
        userDropdown.style.display = "none";
      }
    });
  });
  