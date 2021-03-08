var studentData = [
  { name: "Bob", id: 0, scores: [68, 75, 76, 81] },
  { name: "Alice", id: 1, scores: [75, 90, 64, 88] },
  { name: "Carol", id: 2, scores: [59, 74, 71, 68] },
  { name: "Dan", id: 3, scores: [64, 58, 53, 62] },
];

function processStudentData(data, passThreshold, meritThrehold) {
  passThreshold = typeof passThreshold !== "undefined" ? passThreshold : 60;
  meritThrehold = typeof meritThrehold !== "undefined" ? meritThrehold : 75;

  data.forEach(function (sdata) {
    var av =
      sdata.scores.reduce(function (prev, current) {
        return prev + current;
      }, 0) / sdata.scores.length;
    sdata.average = av;

    if (av > meritThrehold) {
      sdata.assessement = "passed with merit";
    } else if (av > passThreshold) {
      sdata.assessement = "passed";
    } else {
      sdata.assessement = "failed";
    }

    console.log(
      sdata.name +
        "'s(id:" +
        sdata.id +
        ") final assessment is: " +
        sdata.assessement.toUpperCase()
    );
  });
}
processStudentData(studentData);
