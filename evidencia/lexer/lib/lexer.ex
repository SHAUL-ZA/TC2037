# This code is a syntax highlighter made by:
#     Pablo Bolio Pradilla - A01782428
#     Shaul Zayat Askenazi - A01783240
defmodule Lexer do
    @moduledoc """
    Documentation for `Lexer`.
    """
    def marker(in_filename, out_filename) do
      File.mkdir("../Web")
      html_path = ~s(../Web/#{out_filename})
      html_creation(html_path)

      in_filename
      |> File.stream!
      |> Enum.each(&do_marker_line(&1, html_path))

      File.write(html_path, "\n\t\t</pre>\n\t</body>\n</html>", [:append])
      css_creation("../Web/highlighter.css")
    end

    defp html_creation(htmlName) do
      htmlSkeleton = ~s(
        <!DOCTYPE html>
        <html>
          <head>
            <title>Lexer</title>
            <link rel="stylesheet" href="highlighter.css">
          </head>
          <body>
            <pre>)

      File.write(htmlName, htmlSkeleton)
    end


    defp css_creation(cssName) do
      cssSkeleton = ~s|
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
          --errorColor: rgba(249, 68, 73, 0.2);
      }

      body{
          color: #FFFFFF;
          font-family: monospace;
          font-size: 20px;
          background-color: var(--bgColor);
      }

      .comment{ color: var(--commentColor); }

      .variable{ color: var(--variableColor); }

      .boolean{ color: var(--booleanColor); }

      .number{ color: var(--numberColor); }

      .string{ color: var(--stringColor); }

      .arithmetic_op{ color: var(--arithmeticOpColor); }

      .assignment_op{ color: var(--arithmeticOpColor); }

      .comparison_op{ color: var(--arithmeticOpColor); }

      .logical_op{ color: var(--booleanColor); }

      .membership_op{ color: var(--curlyBracketColor);  }

      .identity_op{ color: var(--curlyBracketColor); }

      .bitwise_op{ color: var(--arithmeticOpColor); }

      .endline{ color: var(--stringColor); }

      .tab{ color: var(--stringColor); }

      .parenthesis{ color: var(--parenthesisColor); }

      .bracket{ color: var(--bracketColor); }

      .curly_bracket{ color: var(--curlyBracketColor); }

      .comma{ color: var(--arithmeticOpColor); }

      .colon{ color: var(--arithmeticOpColor); }

      .keyword{ color: var(--keywordColor); }

      .method{ color: var(--methodColor); }

      .attribute_method{ color: var(--methodColor); }

      .error{ background-color: var(--errorColor); }|
      File.write(cssName, cssSkeleton)
    end

    defp do_marker_line(str, out_file) do
        reg_check(str)
        |> case do
            {token, regex} -> create_span(token, regex, str, out_file)
            nil -> File.write(out_file, ~s(<span class="error">#{str}</span>), [:append])
        end
    end

    defp create_span(token, regex, str, out_file) do
        Regex.split(regex, str, trim: true, include_captures: true)
        |>  case do
                [head | []] -> File.write(out_file, ~s(<span class=#{token}>#{head}</span>), [:append])
                [head | [tail | _empty]] -> write_and_recurse(token, head, tail, out_file)
        end
    end

    defp write_and_recurse(token, head, tail, out_file) do
        File.write(out_file, ~s(<span class=#{token}>#{head}</span>), [:append])
        do_marker_line(tail, out_file)
    end

    defp reg_check(str) do
    [{:comment, ~r|^#[^\n]+\|^#\s*|}, # regex that detects comments
     {:string, ~r<^"[^"]*"|^'[^']*'>}, # regex that detects strings
     {:keyword, ~r<(^def|^del|^None|^as|^assert|^break|^class|^continue|^for|^from|^global|^if|^elif|^else|^except|^finally|^import|^lambda|^nonlocal|^pass|^raise|^return|^try|^while|^with|^yield)\b>}, # regex that detects keywords
     {:method, ~r<(^input|^print|^range|^len|^str|^int|^float|^bool|^list|^type)\b>}, # regex that detects methods)
     #{:attribute_method, ~r<\.[a-zA-Z_]\w*>},
     {:membership_op, ~r<(^in|^not in)\b>}, # regex that detects membership operators
     {:identity_op, ~r<(^is|^is not)\b>}, # regex that detects identity operators
     {:logical_op, ~r<(^and|^or|^not)\b>}, # regex that detects logical operators
     {:boolean, ~r<(^True|^False)\b>}, # regex that detects booleans
     {:number, ~r|^[+-]?\d+(\.\d+)?|}, # regex that detects numbers
     {:arithmetic_op, ~r<^\*\*|^\/\/|^\+|^\-|^\*|^\/|^\%>}, # regex that detects arithmetic operators
     {:assignment_op, ~r<^\=|^\*\*\=|^\/\/\=|^\+\=|^\-\=|^\*\=|^\/\=|^\%\=>}, # regex that detects assignment operators
     {:comparison_op, ~r[^\=\=|^\!\=|^\>\=|^\<\=|^\>|^\<]}, # regex that detects comparison operators
     {:bitwise_op, ~r[^\||^\&|^\^|^\~|^\>\>|^\<\<]}, # regex that detects bitwise operators
     {:whitespace, ~r|^\s+|}, # regex that detects whitespaces, tabs and enlines
     {:parenthesis, ~r[^\(|^\)]}, # regex that detects parenthesis
     {:bracket, ~r<^\[|^\]>}, # regex that detects brackets
     {:curly_bracket, ~r<^\{|^\}>}, # regex that detects curly brackets
     {:comma, ~r<^\,>}, # regex that detects commas
     {:colon, ~r<^\:>}, # regex that detects colons
     {:variable, ~r|^[a-zA-Z_]\w*|} # regex that detects variables
    ]
    |> Enum.find(fn {_token, regex} -> Regex.match?(regex, str) end)
    end
  end
