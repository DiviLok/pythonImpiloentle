const form = document.getElementById('add-video-form');
  form.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(form);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/add_video');
    xhr.onload = () => {
      if (xhr.status === 200) {
        alert('Video added successfully!');
      } else {
        alert('Error adding video');
      }
    };
    xhr.send(formData);
  });

  // to add new category to dropdown button
  const selectElement = document.getElementById("category-list");
  const newOption = document.createElement("option");
  newOption.value = "category4";
  newOption.text = "Category 4";
  selectElement.options.add(newOption);
  
