defmodule Lexer do
  @moduledoc """
  Documentation for `Lexer`.
  """
  def marker(in_filename, out_filename) do
    data = in_filename
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
    File.write(htmlName, "\n\t\t</pre>\n\t</body>\n</html>", [:append])
  end


  defp css_creation(cssName) do
    cssSkeleton = ~s<
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
    }>
    File.write(cssName, cssSkeleton)
  end

  defp marker_line(str) do
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

    cond do
      [head | tail] = Regex.split(comment, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{comment}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(variable, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{variable}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(boolean, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{boolean}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(number, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{number}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(string, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{str}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(arithmetic_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{arithmetic_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(assignment_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{assignment_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(comparison_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{comparison_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(logical_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{logical_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(membership_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{membership_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(identity_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{identity_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(bitwise_op, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{bitwise_op}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(whitespace, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{whitespace}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(endline, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{endline}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(tab, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{tab}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(parenthesis, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{parenthesis}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(bracket, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{bracket}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(curly_bracket, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{curly}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(comma, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{comma}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(colon, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{colon}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(keyword, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{keyword}\">#{head}</span>", [:append])
      [head | tail] = Regex.split(method, str, trim: true, include_captures: true) -> File.write("../Web/highlighter.html", "<span class=\"#{method}\">#{head}</span>", [:append])
      true -> File.write("../Web/highlighter.html", "<span class=\"#{"Syntax Error"}\">#{head}</span>", [:append])
    end
  end
end
