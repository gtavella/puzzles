function getMichaelLastName(inputText) {
  var rx = /(?:Michael\s)([A-Z]\w+)/g, a = [];
  while(r = rx.exec(inputText)) a.push(r[1]);
  return a;
}

const inputText = "Michael, how are you? - Cool, how is John Williamns and Michael Jordan? I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James, Michael Green AKA Star and Michael Wood?";

console.log(getMichaelLastName(inputText))
// [ 'Jordan', 'Johnson', 'Green', 'Wood' ]
