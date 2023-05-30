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

  def html_creation(htmlName) do
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

  def css_creation(cssName) do
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
    }

    .body{
        font-family: monospace;
        font-size: 20px;
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


  defp span_tag_creation(htmlName, {spanContent, type}) do
    File.write(htmlName, "<span class=\"#{type}\">#{spanContent}</span>")
  end

    #   defp string_traversal(string, res), do: do_string_traversal(string, [])

  # defp do_string_traversal([], res), do: Enum.reverse(res)
  # defp do_string_traversal([head | tail], res) do
  #   cond do
  #     head =~ comment -> do_string_traversal(tail, [{head, "comment"} | res])
  #     head =~ variable -> do_string_traversal(tail, [{head, "variable"} | res])
  #     head =~ boolean -> do_string_traversal(tail, [{head, "boolean"} | res])
  #     head =~ number -> do_string_traversal(tail, [{head, "number"} | res])
  #     head =~ string -> do_string_traversal(tail, [{head, "string"} | res])
  #     head =~ arithmetic_op -> do_string_traversal(tail, [{head, "arithmetic_op"} | res])
  #     head =~ assignment_op -> do_string_traversal(tail, [{head, "assignment_op"} | res])
  #     head =~ comparison_op -> do_string_traversal(tail, [{head, "comparison_op"} | res])
  #     head =~ logical_op -> do_string_traversal(tail, [{head, "logical_op"} | res])
  #     head =~ membership_op -> do_string_traversal(tail, [{head, "membership_op"} | res])
  #     head =~ identity_op -> do_string_traversal(tail, [{head, "identity_op"} | res])
  #     head =~ bitwise_op -> do_string_traversal(tail, [{head, "bitwise_op"} | res])
  #     head =~ whitespace -> do_string_traversal(tail, [{head, "whitespace"} | res])
  #     head =~ endline -> do_string_traversal(tail, [{head, "endline"} | res])
  #     head =~ tab -> do_string_traversal(tail, [{head, "tab"} | res])
  #     head =~ parenthesis -> do_string_traversal(tail, [{head, "parenthesis"} | res])
  #     head =~ bracket -> do_string_traversal(tail, [{head, "bracket"} | res])
  #     head =~ curly_bracket -> do_string_traversal(tail, [{head, "curly_bracket"} | res])
  #     head =~ comma -> do_string_traversal(tail, [{head, "comma"} | res])
  #     head =~ colon -> do_string_traversal(tail, [{head, "colon"} | res])
  #     head =~ keyword -> do_string_traversal(tail, [{head, "keyword"} | res])
  #     head =~ method -> do_string_traversal(tail, [{head, "method"} | res])
  #     true -> do_string_traversal(tail, [{head, "Invalid Syntax"} | res])
  #   end
  # end
end
