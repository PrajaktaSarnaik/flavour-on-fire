document.getElementById('printButton').addEventListener('click', function() {
    // Clone the content you want to print
    var printContents = document.getElementById('recipeCard').cloneNode(true);

    // Create a temporary div to hold the print content
    var printArea = document.createElement('div');
    printArea.id = 'printArea';
    printArea.style.position = 'absolute';
    printArea.style.top = '0';
    printArea.style.left = '0';
    printArea.style.width = '100%';
    printArea.style.zIndex = '1000';
    printArea.style.backgroundColor = 'white';

    // Append the cloned content to the temporary div
    printArea.appendChild(printContents);
    document.body.appendChild(printArea);

    // Hide the rest of the content on the page
    document.body.style.visibility = 'hidden';
    printArea.style.visibility = 'visible';

    // Trigger the print dialog
    window.print();

    // Restore the original page content after printing
    document.body.style.visibility = 'visible';
    document.body.removeChild(printArea);
});