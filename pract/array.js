// const numbers = [1,2,3]
// const shifted = numbers.shift()

// console.log(numbers)

// console.log(shifted)


// Build a gradebook app using functional programming


function getAverage(scores) {
    let sum = 0
    for (const score of scores) {
        sum += score;
    }
    return sum / scores.length;
}

function getGrade(score) {
    if (score === 100) {
      return "A++";
    } else if (score >= 90) {
      return "A";
    } else if (score >= 80) {
      return "B";
    } else if (score >= 70) {
      return "C";
    } else if (score >= 60) {
      return "D";
    } else {
      return "F";
    }
  }


console.log(hasPassingGrade(100));
console.log(hasPassingGrade(53));
console.log(hasPassingGrade(87));