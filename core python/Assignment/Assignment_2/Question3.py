# Convert distant given in feet and inches into meter and centimeter. 

foot = int(input('Enter the distance in foot:'))
inches = int(input('Enter the distance in inches:'))

# d(m) = d(ft) × 0.3048 + d(in) × 0.0254

meter = (foot * 0.3048) + (inches * 0.0254)

centimeter = meter * 100

print(f' The distance in meter is: {meter}')

print(f'the distance in centimeter is: {centimeter}')



