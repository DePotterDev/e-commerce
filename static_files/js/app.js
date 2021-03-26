var CEP = new Cleave('#id_CEP', {
    numericOnly: true,
    delimiter: '-',
    blocks: [5, 3],
});

var CPF = new Cleave('#id_CPF', {
    numericOnly: true,
    delimiters: ['.', '.', '-'],
    blocks: [3, 3, 3, 2],
});

  