defmodule Lexer do
  @moduledoc """
  Documentation for `Lexer`.
  """

  def marker(in_filename, out_filename) do
    data = in_filname
    |> File.stream!()
    |> Stream.map(&marker_line/1)
    |> Enum.join("")

    File.mkdir("../Web")
    html_creation("../Web/highlighter.html")
    css_creation("../Web/highlighter.css")
  end

  defp html_creation(htmlName) do
    htmlSkeleton = ~s(
      <!`DOCTYPE html>
      <html>
        <head>
          <title>Lexer</title>
          <link rel="stylesheet" href="highlighter.css">
        </head>
        <body>
          <pre>)

    File.write(htmlName, htmlSkeleton)
    span_tag_creation(htmlName, {spanContent, type})
    File.write(htmlName, "\n\t\t</pre>\n\t</body>\n</html>", [:append])

  end

  defp css_creation(cssName) do
    cssSkeleton = ~s(
      :root{
        --keywordColor: #4ec9b0;
        --methodColor: #dcdcaa;
        --curlyBracketColor: #da70d6;
        --parenthesisColor: #179fdb;
        --bracketColor: #ffd710;
        --numberColor: #b5c989;
        --variableColor: #9cdcf0;
        --arithmeticOpColor: #d4d4d4;
        --booleanColor: #569cd6;
        --commentColor: #6a9955;
        --stringColor: #ce9178; /* #ce723c */
        --bgColor: #1f1f1f;
    }

    .body{
        font-family: monospace;
        font-size: 20px;
        background-color: var(--bgColor);
    }

    .comment{
        color: var(--commentColor);
    }

    .variable{
        color: var(--variableColor);
    }

    .boolean{
        color: var(--booleanColor);
    }

    .number{
        color: var(--numberColor);
    }

    .string{
        color: var(--stringColor);
    }

    .arithmetic_op{
        color: var(--arithmeticOpColor);
    }

    .assignment_op{
        color: var(--arithmeticOpColor);
    }

    .comparison_op{
        color: var(--arithmeticOpColor);
    }

    .logical_op{
        color: var(--booleanColor);
    }

    .membership_op{
        color: var(--curlyBracketColor);

    }

    .identity_op{
        color: var(--curlyBracketColor);

    }

    .bitwise_op{
        color: var(--arithmeticOpColor);
    }

    .endline{
        color: var(--stringColor);
    }

    .tab{
        color: var(--stringColor);
    }

    .parenthesis{
        color: var(--parenthesisColor);
    }

    .bracket{
        color: var(--bracketColor);
    }

    .curly_bracket{
        color: var(--curlyBracketColor);
    }

    .comma{
        color: var(--arithmeticOpColor);
    }

    .colon{
        color: var(--arithmeticOpColor);
    }

    .keyword{
        color: var(--keywordColor);
    }

    .method{
        color: var(--methodColor);
    }
    )

    File.write(cssName, cssSkeleton)

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


  defp span_tag_creation(htmlName, {type, spanContent}) do
    File.write(htmlName, "<span class=\"#{type}\">#{spanContent}</span>", [:append])
  end # can be an arrow function in a map

  {spanContent, type}

  # [head | tail] = Regex.split(regex, string, trim: true, include_captures: true) # this be what matches regex and makes it into head and tail

  defp string_traversal(string, res), do: do_string_traversal(string, [])

  defp do_string_traversal("", res), do: Enum.reverse(res)
  defp do_string_traversal(string, res) do
    cond do
      [head | tail] = Regex.split(comment, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "comment"} | res])
      [head | tail] = Regex.split(variable, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "variable"} | res])
      [head | tail] = Regex.split(boolean, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "boolean"} | res])
      [head | tail] = Regex.split(number, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "number"} | res])
      [head | tail] = Regex.split(string, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "string"} | res])
      [head | tail] = Regex.split(arithmetic_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "arithmetic_op"} | res])
      [head | tail] = Regex.split(assignment_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "assignment_op"} | res])
      [head | tail] = Regex.split(comparison_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "comparison_op"} | res])
      [head | tail] = Regex.split(logical_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "logical_op"} | res])
      [head | tail] = Regex.split(membership_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "membership_op"} | res])
      [head | tail] = Regex.split(identity_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "identity_op"} | res])
      [head | tail] = Regex.split(bitwise_op, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "bitwise_op"} | res])
      [head | tail] = Regex.split(whitespace, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "whitespace"} | res])
      [head | tail] = Regex.split(endline, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "endline"} | res])
      [head | tail] = Regex.split(tab, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "tab"} | res])
      [head | tail] = Regex.split(parenthesis, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "parenthesis"} | res])
      [head | tail] = Regex.split(bracket, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "bracket"} | res])
      [head | tail] = Regex.split(curly, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "curly_bracket"} | res])
      [head | tail] = Regex.split(comma, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "comma"} | res])
      [head | tail] = Regex.split(colon, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "colon"} | res])
      [head | tail] = Regex.split(keyword, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "keyword"} | res])
      [head | tail] = Regex.split(method, string, trim: true, include_captures: true) -> do_string_traversal(tail, [{head, "method"} | res])
      true -> do_string_traversal(tail, [{head, "Invalid Syntax"} | res]) # this has to be checked if the rest of the cond works
    end
  end
end
