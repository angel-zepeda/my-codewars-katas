function list(names) {
  let result = []
  if (names[0] === undefined) return '';
  if (names.length === 1)  return names[0].name;
  for (let i = 0; i < names.length -1; i++) {
    const comma = i === names.length-2 ? '' : ', '
    result.push(names[i].name + comma)
  }
  result.push(' & ' + names[names.length -1].name)
  return result.join('')
}
