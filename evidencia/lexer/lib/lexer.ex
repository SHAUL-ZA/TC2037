defmodule Lexer do
  @moduledoc """
  Documentation for `Lexer`.
  """

  def marker(in_filename, out_filename) do
    data = in_filname
    |> File.stream!()
    |> Stream.map(&marker_line/1)
    |> Enum.join("")

    File.write(out_filename, data)
  end



  defp marker_line(string) do
    comment = ~r|^#[^\n]+|
    variable = ~r|^[a-zA-Z_]\w*|
    boolean = ~r<^True|^False>
    number = ~r|^[+-]?\d+(\.\d+)?|
    string = ~r<^"[^"]*"|^'[^']*'>
    arithmetic_op = ~r<^\*\*|^\/\/|^\+|^\-|^\*|^\/|^\%>
    assignment_op = ~r<^\=|^\*\*\=|^\/\/\=|^\+\=|^\-\=|^\*\=|^\/\=|^\%\=>
    comparison_op = ~r[^\=\=|^\!\=|^\>\=|^\<\=|^\>|^\<]
    logical_op = ~r<^and|^or|^not>
    membership_op = ~r<^in|^not in>
    identity_op = ~r<^is|^is not>
    bitwise_op = ~r[^\||^\&|^\^|^\~|^\>\>|^\<\<]
    whitespace = ~r|^\s+|
    endline = ~r|^\n|
    tab = ~r|^\t|
    parenthesis = ~r[^\(|^\)]
    bracket = ~r<^\[|^\]>
    curly_bracket = ~r<^\{|^\}>
    comma = ~r<^\,>
    colon = ~r<^\:>
    keyword = ~r<^def|^del|^None|^as|^assert|^break|^class|^continue|^for|^from|^global|^if|^elif|^else|^except|^finally|^import|^lambda|^nonlocal|^pass|^raise|^return|^try|^while|^with|^yield>
    method = ~r<^input|^print|^range|^len|^str|^int|^float|^bool|^list|^type>

    defp string_traversal(string, res), do: do_string_traversal(string, [])

  defp do_string_traversal([], res), do: Enum.reverse(res)
  defp do_string_traversal([head | tail], res) do
    cond do
      head =~ comment -> do_string_traversal(tail, [{head, "comment"} | res])
      head =~ variable -> do_string_traversal(tail, [{head, "variable"} | res])
      head =~ boolean -> do_string_traversal(tail, [{head, "boolean"} | res])
      head =~ number -> do_string_traversal(tail, [{head, "number"} | res])
      head =~ string -> do_string_traversal(tail, [{head, "string"} | res])
      head =~ arithmetic_op -> do_string_traversal(tail, [{head, "arithmetic_op"} | res])
      head =~ assignment_op -> do_string_traversal(tail, [{head, "assignment_op"} | res])
      head =~ comparison_op -> do_string_traversal(tail, [{head, "comparison_op"} | res])
      head =~ logical_op -> do_string_traversal(tail, [{head, "logical_op"} | res])
      head =~ membership_op -> do_string_traversal(tail, [{head, "membership_op"} | res])
      head =~ identity_op -> do_string_traversal(tail, [{head, "identity_op"} | res])
      head =~ bitwise_op -> do_string_traversal(tail, [{head, "bitwise_op"} | res])
      head =~ whitespace -> do_string_traversal(tail, [{head, "whitespace"} | res])
      head =~ endline -> do_string_traversal(tail, [{head, "endline"} | res])
      head =~ tab -> do_string_traversal(tail, [{head, "tab"} | res])
      head =~ parenthesis -> do_string_traversal(tail, [{head, "parenthesis"} | res])
      head =~ bracket -> do_string_traversal(tail, [{head, "bracket"} | res])
      head =~ curly_bracket -> do_string_traversal(tail, [{head, "curly_bracket"} | res])
      head =~ comma -> do_string_traversal(tail, [{head, "comma"} | res])
      head =~ colon -> do_string_traversal(tail, [{head, "colon"} | res])
      head =~ keyword -> do_string_traversal(tail, [{head, "keyword"} | res])
      head =~ method -> do_string_traversal(tail, [{head, "method"} | res])
      true -> do_string_traversal(tail, [{head, "Invalid Syntax"} | res])
    end
  end


  cond do
    head =~ comment -> "comment"
    head =~ variable -> "variable"
    head =~ boolean -> "boolean"
    head =~ number -> "number"
    head =~ string -> "string"
    head =~ arithmetic_op -> "arithmetic_op"
    head =~ assignment_op -> "assignment_op"
    head =~ comparison_op -> "comparison_op"
    head =~ logical_op -> "logical_op"
    head =~ membership_op -> "membership_op"
    head =~ identity_op -> "identity_op"
    head =~ bitwise_op -> "bitwise_op"
    head =~ whitespace -> "whitespace"
    head =~ endline -> "endline"
    head =~ tab -> "tab"
    head =~ parenthesis -> "parenthesis"
    head =~ bracket -> "bracket"
    head =~ curly_bracket -> "curly_bracket"
    head =~ comma -> "comma"
    head =~ colon -> "colon"
    head =~ keyword -> "keyword"
    head =~ method -> "method"
    true -> "Invalid Syntax"
  end
  end



end
