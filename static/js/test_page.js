const all_tests = document.querySelectorAll(`.listQ`);

document.querySelector(`.btn`).addEventListener(`click`, (e) => {
  let wrong_ans = 0;
  let correct_ans = 0;

  e.preventDefault();
  all_tests.forEach((i) => {
    const correct = i.children[3];
    const answer = i.children[2];

    if (answer.value.trim() === correct.textContent) {
      correct_ans++;
      correct.classList.remove(`hidden`);
      correct.classList.remove(`wrong`);
      correct.classList.add(`correct`);
    } else {
      wrong_ans++;
      correct.classList.remove(`hidden`);
      correct.classList.remove(`correct`);
      correct.classList.add(`wrong`);
    }

    const logg = document.querySelector(`.listecQ`);

    logg.classList.remove(`hidden`);

    const correct_display = logg.children[1];
    const wrong_display = logg.children[3];
    const grade = logg.children[4].children[0];
    const percentage = logg.children[4].children[2];

    const grades = {
      1: 91,
      2: 81,
      3: 71,
      4: 61,
      5: 0,
    };

    const makepercentage = (correctQ, allQ) => {
      return Math.floor((100 / allQ) * correctQ);
    };

    const percentageValue = makepercentage(
      correct_ans,
      correct_ans + wrong_ans
    );

    const get_grade = (percentage) => {
      for (let [key, value] of Object.entries(grades)) {
        console.log(key, value);

        if (percentage >= value) {
          return key;
        }
      }
    };

    correct_display.textContent = correct_ans;
    wrong_display.textContent = wrong_ans;
    percentage.textContent = percentageValue + `%`;
    grade.textContent = get_grade(percentageValue);
  });
});
