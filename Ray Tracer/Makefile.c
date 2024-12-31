all: Final

Final: final.o vector.o spheres.o color.o
	gcc -Wall -Werror -std=c99 -o Final final.o vector.o spheres.o color.o -lm

final.o: src/assg.c src/vector.h src/spheres.h src/color.h
	gcc -Wall -Werror -std=c99 -c src/assg.c -o final.o

vector.o: src/vector.c src/vector.h
	gcc -Wall -Werror -std=c99 -c src/vector.c

spheres.o: src/spheres.c src/spheres.h src/vector.h
	gcc -Wall -Werror -std=c99 -c src/spheres.c

color.o: src/color.c src/color.h src/vector.h
	gcc -Wall -Werror -std=c99 -c src/color.c

clean:
	rm -f *.o MS1_assg MS2_assg FS_assg