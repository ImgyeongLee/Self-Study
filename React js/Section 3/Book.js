import React from "react";

const Book = ({ image, title, author }) => {
  const clickHandler = () => {
    alert("Hello World!");
  };
  const complexExample = (author) => {
    alert(author);
  };

  return (
    <article
      className="book"
      onMouseOver={() => {
        console.log(title);
      }}
    >
      <img src={image} alt="" />
      <h1 onClick={() => console.log(title)}>{title}</h1>
      <h4>{author}</h4>
      <button type="button" onClick={clickHandler}>
        reference example
      </button>
      <button
        type="button"
        // If you do not put ()=>,
        // then you will invoke the function
        // when you run your application
        onClick={() => complexExample(author)}
      >
        more complex example
      </button>
    </article>
  );
};
export default Book;
