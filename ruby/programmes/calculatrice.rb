def addition(a, b)
  a + b
end

def soustraction(a, b)
  a - b
end

def multiplication(a, b)
  a * b
end

def division(a, b)
  if b == 0
    "Erreur : division par zéro"
  else
    a / b.to_f
  end
end

# Programme principal
loop do
  puts "\n--- Mini Calculatrice ---"
  puts "1. Addition"
  puts "2. Soustraction"
  puts "3. Multiplication"
  puts "4. Division"
  puts "5. Quitter"
  print "Choisissez une option : "
  choix = gets.chomp.to_i

  break if choix == 5

  print "Entrez le premier nombre : "
  a = gets.chomp.to_f
  print "Entrez le deuxième nombre : "
  b = gets.chomp.to_f

  case choix
  when 1
    puts "Résultat = #{addition(a, b)}"
  when 2
    puts "Résultat = #{soustraction(a, b)}"
  when 3
    puts "Résultat = #{multiplication(a, b)}"
  when 4
    puts "Résultat = #{division(a, b)}"
  else
    puts "Option invalide"
  end
end
