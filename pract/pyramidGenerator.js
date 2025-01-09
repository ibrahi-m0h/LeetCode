// Create a pyramid using #'s in which each row there is n+1 #'s up to 8

const character = "#"
const count = 8
const rows = []

for (let i = 0; i < count; i++){
    rows.push(character.repeat(i))
}

console.log(rows.join('\n'))
