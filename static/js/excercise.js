const questions = document.querySelectorAll(`.excQ`);

questions.forEach((i) => {
  const btn = i.children[2].children[1];

  alert(1)

  btn.addEventListener(`click`, (e) => {

  alert (2)

    e.preventDefault();

  alert(3)

    const parent = e.path[2].children[2].children;
    alert(4)
    const answer = e.path[2].children[3];
    alert(5)
    const text = parent[0];
    alert(6)

    if (text.value.trim() === answer.textContent) {
      alert(7)
      answer.classList.remove(`hidden`);
      answer.classList.remove(`wrong`);
      answer.classList.add(`correct`);
    } else {
      alert(8)
      answer.classList.remove(`hidden`);
      answer.classList.remove(`correct`);
      answer.classList.add(`wrong`);
    }
  });
});
alert(9)