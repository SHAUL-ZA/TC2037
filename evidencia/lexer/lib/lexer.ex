defmodule Lexer do
  @moduledoc """
  Documentation for `Lexer`.
  """

  def marker(in_filename, out_filename, offset) do
    data = in_filname
    |> File.stream!()
    |> Stream.map(&marker_line(&1, offset))
    |> Enum.join("")

    File.write(out_filename, data)


  end

  defp marker_line(string) do
    comment = ~r|^(#[^\n]+)|
    variable = ~r|^([a-zA-Z_]\w*)|
    boolean = ~r|^(True|False)|
    number = ~r|^[+-]?\d+(\.\d+)?|
    string = ~r|^("[^"]*"|'[^']*')|
    arithmetic_op = ~r|^((\*\*)|(\/\/)|\+|\-|\*|\/|\%)|
    assignment_op = ~r|^((\=)|(\*\*\=)|(\/\/\=)|(\+\=)|(\-\=)|(\*\=)|(\/\=)|(\%\=))|
    comparison_op = ~r|^((\=\=)|(\!\=)|(\>\=)|(\<\=)|(\>)|(\<))|
    logical_op = ~r<^(and|or|not)>
    membership_op = ~r|^(in|not in)|
    identity_op = ~r|^(is|is not)|
    bitwise_op = ~r<^(\||\&|\^|\~|(\>\>)|(\<\<))>
    whitespace = ~r|^(\s+)|
    endline = ~r|^(\n)|
    tab = ~r|^(\t)|
    parenthesis = ~r|^(\(|\))|
    bracket = ~r|^(\[|\])|
    curly_bracket = ~r|^(\{|\})|
    comma = ~r|^(\,)|
    colon = ~r|^(\:)|
    keyword = ~r|^(def|del|None|as|assert|break|class|continue|for|from|global|if|elif|else|except|finally|import|lambda|nonlocal|pass|raise|return|try|while|with|yield)|
    method = ~r|^(input|print|range|len|str|int|float|bool|list|type)|
  end

end
