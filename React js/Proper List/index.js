import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

const books = [
  {
    image:
      "https://images-na.ssl-images-amazon.com/images/I/81eB%2B7%2BCkUL._AC_UL200_SR200,200_.jpg",
    title: "I Love You to the Moon and Back",
    author: "Amelia Hepworth",
  },
  {
    image:
      "https://images-na.ssl-images-amazon.com/images/I/71aLultW5EL._AC_UL200_SR200,200_.jpg",
    title: "Our Class is a Family",
    author: "Shannon Oisen",
  },
  {
    image:
      "https://images-na.ssl-images-amazon.com/images/I/617uZq23IPL._AC_UL200_SR200,200_.jpg",
    title: "Reminders of Him: A Novel",
    author: "Colleen Hoover",
  },
];

function BookList() {
  return (
    <section className="booklist">
      {books.map((book) => {
        return <Book book={book} />;
      })}
    </section>
  );
}
const Book = (props) => {
  const { image, title, author } = props.book;
  return (
    <article className="book">
      <img src={image} alt=" " />
      <h1>{title}</h1>
      <h4>{author}</h4>
    </article>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BookList />
  </React.StrictMode>
);
