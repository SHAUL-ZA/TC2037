# This code is a syntax highlighter made by:
#     Pablo Bolio Pradilla - A01782428
#     Shaul Zayat Askenazi - A01783240
defmodule Lexer do
    @moduledoc """
    Documentation for `Lexer`.

    ## Authors

    Pablo Bolio Pradilla - A01782428

    Shaul Zayat Askenazi - A01783240

    Contains code for a syntax highlighter.
    The only public function is marker, which
    expects a path to a python file and a name
    for the output html file.
    """

    @doc """
    Creates a new html file in a new directory called
    Web, then it will read the file that was
    passed as an argument and recursively
    write spans for it to be propetly highlighted.
    After this the html is closed and the css file
    is created.
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

    @doc """
    Documentation for `html_creation`.

    This function creates the skeleton
    of the html file but doesn't close
    it in order to fill it with the
    python code.
    """
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

    @doc """
    Documentation for `css_creation`.

    This function creates the css file itself.
    """
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

    @doc """
    Documentation for `do_marker_line`.

    This function receives a certain string,
    that in this case will be given by the
    external file through a stream in the
    function that merges it all (marker),
    and it will pipe a regex check to see
    if it matches any of the tokens, if it
    does, it will call the create_span function.
    If it doesn't, it will write a span tag
    with the error class and the unmatched string.
    """
    defp do_marker_line(str, out_file) do
        reg_check(str)
        |> case do
            {token, regex} -> create_span(token, regex, str, out_file)
            nil -> File.write(out_file, ~s(<span class="error">#{str}</span>), [:append])
        end
    end

    @doc """
    Documentation for `create_span`.

    This function receives a token, a regex,
    a string and the output file name, it will
    split the string using the regex.split() method
    and pipe it to a case, if the list has only
    a head part and not a tail, then it will
    write a span tag with the last token class
    that was found and the head part of the list.
    If it has a tail, it will the recursive function
    that makes everything fall into place.
    """
    defp create_span(token, regex, str, out_file) do
        Regex.split(regex, str, trim: true, include_captures: true)
        |>  case do
                [head | []] -> File.write(out_file, ~s(<span class=#{token}>#{head}</span>), [:append])
                [head | [tail | _empty]] -> write_and_recurse(token, head, tail, out_file)
        end
    end

    @doc """
    Documentation for `write_and_recurse`.

    This function receives a token, a head, a tail
    and the output file name, with that, it will
    write a span tag with the token class and the
    head part of the list, and then it will call
    the do_marker_line function with the tail part
    acting as the string and keeping the output file
    name, so it recursively writes on the html file
    until the given string is empty.
    """
    defp write_and_recurse(token, head, tail, out_file) do
        File.write(out_file, ~s(<span class=#{token}>#{head}</span>), [:append])
        do_marker_line(tail, out_file)
    end

    @doc """
    Documentation for `reg_check`.

    This function receives a string and creates a list
    of tuples with the token name and the regex that
    will be used to check if the string matches any of
    the tokens, if it does, it will return a tuple with
    the token name and the regex, if it doesn't, it will
    return nil, this is all achieved using the Enum.find
    method and an anonymous function that pipes the string
    to a Regex.match?() method.
    """
    defp reg_check(str) do
    [{:comment, ~r|^#[^\n]+\|^#\s*|}, # regex that detects comments
     {:string, ~r<^"[^"]*"|^'[^']*'>}, # regex that detects strings
     {:keyword, ~r<(^def|^del|^None|^as|^assert|^break|^class|^continue|^for|^from|^global|^if|^elif|^else|^except|^finally|^import|^lambda|^nonlocal|^pass|^raise|^return|^try|^while|^with|^yield)\b>}, # regex that detects keywords
     {:method, ~r<(^input|^print|^range|^len|^str|^int|^float|^bool|^list|^type)\b>}, # regex that detects methods)
     {:attribute_method, ~r<^\.[a-zA-Z_]\w*>},
     {:membership_op, ~r<(^in|^not in)\b>}, # regex that detects membership operators
     {:identity_op, ~r<(^is|^is not)\b>}, # regex that detects identity operators
     {:logical_op, ~r<(^and|^or|^not)\b>}, # regex that detects logical operators
     {:boolean, ~r<(^True|^False)\b>}, # regex that detects booleans
     {:parenthesis, ~r[^\(|^\)]}, # regex that detects parenthesis
     {:number, ~r|^[+-]?\d+(\.\d+)?|}, # regex that detects numbers
     {:arithmetic_op, ~r<^\*\*|^\/\/|^\+|^\-|^\*|^\/|^\%>}, # regex that detects arithmetic operators
     {:assignment_op, ~r<^\=|^\*\*\=|^\/\/\=|^\+\=|^\-\=|^\*\=|^\/\=|^\%\=>}, # regex that detects assignment operators
     {:comparison_op, ~r[^\=\=|^\!\=|^\>\=|^\<\=|^\>|^\<]}, # regex that detects comparison operators
     {:bitwise_op, ~r[^\||^\&|^\^|^\~|^\>\>|^\<\<]}, # regex that detects bitwise operators
     {:whitespace, ~r|^\s+|}, # regex that detects whitespaces, tabs and enlines
     {:bracket, ~r<^\[|^\]>}, # regex that detects brackets
     {:curly_bracket, ~r<^\{|^\}>}, # regex that detects curly brackets
     {:comma, ~r<^\,>}, # regex that detects commas
     {:colon, ~r<^\:>}, # regex that detects colons
     {:variable, ~r|^[a-zA-Z_]\w*|} # regex that detects variables
    ]
    |> Enum.find(fn {_token, regex} -> Regex.match?(regex, str) end)
    end
  end
