const firstInput = document.getElementById("firstNumber");
const secondInput = document.getElementById("secondNumber");
const resultValue = document.getElementById("resultValue");
const resultHint = document.getElementById("resultHint");
const operationButtons = document.querySelectorAll("[data-operation]");

const operationLabels = {
  "+": "сложить",
  "-": "вычесть",
  "*": "умножить",
  "/": "разделить",
};

const operationDescriptions = {
  "+": "Складываем два числа и получаем сумму.",
  "-": "Вычитаем второе число из первого.",
  "*": "Умножаем первое число на второе.",
  "/": "Делим первое число на второе.",
};

const formatNumber = (value) => {
  if (Number.isNaN(value)) {
    return "Ошибка";
  }

  return new Intl.NumberFormat("ru-RU", {
    maximumFractionDigits: 4,
  }).format(value);
};

const parseInput = (input) => {
  const value = Number.parseFloat(input.value);
  return Number.isNaN(value) ? null : value;
};

const updateResult = (operation) => {
  const first = parseInput(firstInput);
  const second = parseInput(secondInput);

  if (first === null || second === null) {
    resultValue.textContent = "Проверьте оба числа";
    resultHint.textContent = "Введите два числа, чтобы продолжить.";
    return;
  }

  if (operation === "/" && second === 0) {
    resultValue.textContent = "Деление на ноль невозможно";
    resultHint.textContent = "Попробуйте другое второе число.";
    return;
  }

  let result = 0;
  switch (operation) {
    case "+":
      result = first + second;
      break;
    case "-":
      result = first - second;
      break;
    case "*":
      result = first * second;
      break;
    case "/":
      result = first / second;
      break;
    default:
      result = 0;
  }

  resultValue.textContent = formatNumber(result);
  resultHint.textContent = `${operationDescriptions[operation]} (${first} ${operation} ${second} = ${formatNumber(result)})`;
};

operationButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const operation = button.dataset.operation;
    resultValue.textContent = `Готово: ${operationLabels[operation]}`;
    resultHint.textContent = operationDescriptions[operation];
    updateResult(operation);
  });
});

[firstInput, secondInput].forEach((input) => {
  input.addEventListener("input", () => {
    resultValue.textContent = "Введите числа";
    resultHint.textContent = "Выберите операцию, чтобы увидеть объяснение.";
  });
});
