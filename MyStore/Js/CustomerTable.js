// Executes when document is loaded
document.addEventListener("DOMContentLoaded", (ev) => {
    
    document.getElementById("customer-info--table").appendChild(buildTableBody());
  
  
  });
  
  // Document Builder
  const buildTableBody = () => {
    const Customers = CUSTOMERS_INFO_DATA;
  
    const tbody = document.createElement("tbody");
  
    let bodyContent = "";
    for (const row of Customers) {
      bodyContent += `
     
        <tr>
          <td>${row.Name}</td>
          <td>${row.Number}</td>
          <td>${row.City}</td>
          <td ${row.Orders}</td>
          
        </tr>
      `;
    }
  
    tbody.innerHTML = bodyContent;
  
    return tbody;
  };
  
  
  // Document operation functions
  const sideMenu = document.querySelector("aside");
  const menuBtn = document.querySelector("#menu-btn");
  const closeBtn = document.querySelector("#close-btn");
  const themeToggler = document.querySelector(".theme-toggler");
  
  // Show Sidebar
  menuBtn.addEventListener("click", () => {
    sideMenu.style.display = "block";
  });
  
  // Hide Sidebar
  closeBtn.addEventListener("click", () => {
    sideMenu.style.display = "none";
  });
  
  // Change Theme
  themeToggler.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme-variables");
  
    themeToggler.querySelector("span:nth-child(1)").classList.toggle("active");
    themeToggler.querySelector("span:nth-child(2)").classList.toggle("active");
  });