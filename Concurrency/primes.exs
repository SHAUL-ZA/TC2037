# Module for finding prime numbers in a range and summing them by using parallelism
# Authors:
#   Pablo Bolio Pradilla - A01782428
#   Shaul Zayat Askenazi - A01783240
# 06/12/2023
defmodule Hw do

  def make_ranges(start, finish, threads) do
    #Take the range and split it into a list of ranges for each thread to process in parallel
    range_size = finish - start + 1
    range_size_per_thread = div(range_size, threads) # div is integer division
    Enum.map(0..(threads-1), fn (thread) ->
      {start + thread * range_size_per_thread, start + (thread + 1) * range_size_per_thread - 1} # the last range may be smaller than the others
    end)
  end



  #find and sum all prime number in a range
  def sum_prime({start, finish}) do
    do_sum_prime(start, finish, 0)
  end

  defp do_sum_prime(start, finish, total) when start > finish, do: total
  defp do_sum_prime(start, finish, total) do
    if is_prime(start, 2) do
      do_sum_prime(start + 1, finish, total + start)
    else
      do_sum_prime(start + 1, finish, total)
    end
  end

  def is_prime(n, counter) do
    cond do
      n < 2 -> false
      n == 2 -> true
      rem(n, counter) == 0 -> false
      counter >= :math.sqrt(n) -> true
      true -> is_prime(n, counter + 1)
    end
  end

  # :math.sqrt(n)
  # |> round()
  # :timer.tc(fn -> <funcion a medir> |> elem(0) |> Kernel./(1000000) end)

  # def my_map([], _func), do: []
  # def my_map([head | tail], func) do
  #   [func.(head) | my_map(tail, func)]
  # end

  # def sum_list([]), do: 0
  # def sum_list([head | tail]) do
  #   head + sum_list(tail)
  # end



  def prime_sum(start, finish, threads) do
    IO.puts("Main thread starting")
    make_ranges(start, finish, threads)
    |> IO.inspect()
    |> Enum.map(&Task.async(fn -> sum_prime(&1) end))
    |> Enum.map(&Task.await(&1, :infinity))
    |> IO.inspect()
    |> Enum.sum()
  end


end
