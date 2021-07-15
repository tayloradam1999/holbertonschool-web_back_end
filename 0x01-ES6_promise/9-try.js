export default function guardrail(mathFunction) {
  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (Error) {
    return [`Error: ${Error.message}`, 'Guardrail was processed'];
  }
}
