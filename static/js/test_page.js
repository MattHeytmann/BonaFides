const all_tests = document.querySelectorAll(`.listQ`);

document.querySelector(`.btn`).addEventListener(`click`, (e) => {

    let wrong_ans = 0
    let correct_ans = 0

  e.preventDefault();
  all_tests.forEach((i) => {

    const correct = i.children[3];
    const answer = i.children[2];


    if (answer.value.trim() === correct.textContent) {
      correct_ans ++
      correct.classList.remove(`hidden`);
      correct.classList.remove(`wrong`);
      correct.classList.add(`correct`);
    } else {
        wrong_ans ++
      correct.classList.remove(`hidden`);
      correct.classList.remove(`correct`);
      correct.classList.add(`wrong`);
    }

    const logg = document.querySelector(`.listecQ`)

    logg.classList.remove(`hidden`)

    const correct_display = logg.children[1]
    const wrong_display = logg.children[3]

    correct_display.textContent = correct_ans
    wrong_display.textContent = wrong_ans

    console.log(logg);

  });
});
