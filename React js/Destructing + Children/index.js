import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

const firstBook = {
  img: "https://images-na.ssl-images-amazon.com/images/I/81eB%2B7%2BCkUL._AC_UL200_SR200,200_.jpg",
  title: "I Love You to the Moon and Back",
  author: "Amelia Hepworth",
};

const secondBook = {
  img: "https://images-na.ssl-images-amazon.com/images/I/71aLultW5EL._AC_UL200_SR200,200_.jpg",
  title: "Our Class is a Family",
  author: "Shannon Oisen",
};

function BookList() {
  return (
    <section className="booklist">
      <Book
        image={firstBook.img}
        title={firstBook.title}
        author={firstBook.author.toUpperCase()}
      >
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, Dolore cum
          animi voluptas temporibus quo delectus pariatur, hic voluptatum
          accusantium illo.
        </p>
      </Book>
      <Book
        image={secondBook.img}
        title={secondBook.title}
        author={secondBook.author.toUpperCase()}
      />
    </section>
  );
}
const Book = ({ image, title, author, children }) => {
  // const { img, title, author } = props;
  return (
    <article className="book">
      <img src={image} alt=" " />
      <h1>{title}</h1>
      <h4>{author}</h4>
      {children}
    </article>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BookList />
  </React.StrictMode>
);
