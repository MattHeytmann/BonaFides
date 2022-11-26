const questions = document.querySelectorAll(`.excQ`);

questions.forEach((i) => {
  const btn = i.children[2].children[1];

  btn.addEventListener(`click`, (e) => {
    e.preventDefault();

    const parent = e.path[2].children[2].children;
    const answer = e.path[2].children[3];
    const text = parent[0];

    alert(text, answer, parent)

    if (text.value.trim() === answer.textContent) {
      answer.classList.remove(`hidden`);
      answer.classList.remove(`wrong`);
      answer.classList.add(`correct`);
    } else {
      answer.classList.remove(`hidden`);
      answer.classList.remove(`correct`);
      answer.classList.add(`wrong`);
    }
  });
});
