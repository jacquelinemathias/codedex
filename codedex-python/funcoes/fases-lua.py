# Write a moon_phase() function that takes in a phase parameter of the Moon phase name given below and returns the correct Moon emoji for it:

#     New Moon → 🌑
#     Waxing Crescent → 🌒
#     First Quarter → 🌓
#     Waxing Gibbous → 🌔
#     Full Moon → 🌕
#     Waning Gibbous → 🌖
#     Last Quarter → 🌗
#     Waning Crescent → 🌘

# Else an invalid phase name is passed to moon_phase(), return 'Invalid moon phase'.

# Call the moon_phase() to test it out.

def fases_lua():
    fase = input('Informe o nome de uma fase da lua: ')
    if fase == 'Lua Nova' or fase == 'Nova':
        return('🌑')
    elif fase == 'Lua Minguante' or fase == 'Minguante':
        return('🌒')
    elif fase == 'Quarto Minguante':
        return('🌓')
    elif fase == 'Minguante Gibosa':
        return('🌔')
    elif fase == 'Lua Cheia' or fase == 'Cheia':
        return('🌕')
    elif fase == 'Crescente Gibosa':
        return('🌖')
    elif fase == 'Quarto Crescente':
        return('🌗')
    elif fase == 'Lua Crescente' or fase == 'Crescente':
        return('🌘')
    else:
        return('Fase inválida!')

lua = fases_lua()
print(lua)