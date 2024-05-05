document.addEventListener('DOMContentLoaded', function() {
    const collapsibleHeaders = document.querySelectorAll('.collapsible-header');
  
    collapsibleHeaders.forEach(function(header) {
      header.addEventListener('click', function() {
        const content = header.nextElementSibling;
        content.classList.toggle('show');
      });
    });
  });