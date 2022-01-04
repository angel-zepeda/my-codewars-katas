function anagrams(word, words) {
  const anagrams = []

  const newWord = word.split('').sort().join('');

  for (const w of words) {
    let wordToEval = w.split('').sort().join('');
    if (newWord === wordToEval) {
      anagrams.push(w)
    }
  }
  return anagrams;
}


console.log(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']));
console.log(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
console.log(anagrams('laser', ['lazing', 'lazy',  'lacer']));
