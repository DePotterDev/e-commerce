var CEP = new Cleave('#id_CEP', {
    // numeral: true,
    delimiter: '-',
    blocks: [5, 3],
});

var CPF = new Cleave('#id_CPF', {
    delimiters: ['.', '.', '-'],
    blocks: [3, 3, 3, 2],
});

  