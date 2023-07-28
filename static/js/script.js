const option = document.getElementById("option")
const bookOption = document.querySelectorAll("#book-option")

if (option) {
  option.onchange = (e) => {
    const selectedOption = e.target.value
    bookOption.forEach(option => {
      const bookAuthors = convert(option.getAttribute("data-author"))
      const bookCategories = convert(option.getAttribute("data-category"))

      if (
        selectedOption !== ""
        && bookAuthors.includes(selectedOption)
        || bookCategories.includes(selectedOption)
      ) {
        option.selected = "selected"
      } else {
        option.selected = ""
      }
    })
  }
}

function convert(str) {
  const regex = /(Author: |Category: |QuerySet |<|>|\[|\])/g;
  str = str.replace(regex, "");
  return str.split(", ");
}
