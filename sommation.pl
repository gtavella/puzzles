/* CASI GENERALI DI SOMMATORIA E PRODUTTORIA
 * Posso costruire il caso piu' semplice di sommatoria e produttoria.
 * Ovvero sommatoria da 0 a N. Cioe' sommo 1+2+3...+(N-1)+N 
 * Stesso discorso per la produttoria. 1*2*3...*(N-1)*N 
 * Ma se voglio partire da un altro indice? 
 * Cosa faccio se l' i-esimo termine e' piu' complesso? Ad esempio (2*i)/(3+i) ecc.
 * Per questo motivo mi sono costruito dei casi piu' generali 
 * */

% Per cambiare l'addendo/fattore (cioe' il singolo termine) dell'operazione 
% sommatoria/produttoria, basta cambiare il contenuto del predicato addendo/fattore


% SOMMATORIA da I a N, con J indice mobile
%           >> cambia qui sotto dopo is.. <<                    
addendo(J,R):- R is (J*2)/3.
% l'ultimo termine
sommatoria(I,I,R):- addendo(I,R).
% tutti gli altri casi
sommatoria(I,N,R):- N>I, addendo(I,R1), J is I+1, sommatoria(J,N,R2), R is R1+R2.



% PRODUTTORIA da I a N, con J indice mobile
%          >> cambia qui sotto dopo is.. <<               
fattore(J,R):- R is (J-1)/2.
% l'ultimo termine
produttoria(I,I,R):- fattore(I,R).
% tutti gli altri casi
produttoria(I,N,R):- N>I, fattore(I,R1), J is I+1, produttoria(J,N,R2), R is R1*R2.


% Nota:
% (A)
% considero solo il caso in cui il generico termine dipende solo dall'indice mobile J. 
% In poche parole non includo il caso in cui il generico termine possa dipendere da I o N 
% cioe' i valori fissi (I=dove comincio, N=dove finisco). 
% (B)
% Inoltre non considero i casi in cui I=0, perche' anche in quel caso il termine potrebbe 
% avere avere senso, ad esempio per I=0, ((2*I)+3)/(3-I) = 3/3 = 1 
% ma non ha senso per 2*3*I=0 (mi annulla il prodotto) oppure (5+I)/I (non posso dividere per 0) ecc.  
% Quindi sta a te includere indici che abbiano senso 



% CASI SPECIFICI
% per ottenere nuove sommatorie o produttorie, 
% ricordati sempre di cambiare il generico termine (addendo/fattore)
% se vuoi fare una semplice sommatoria o produttoria, il termine deve essere semplicemente J
% quindi R is J
%sommatoria(0,N,X). % sommatoria da 0 a N
%produttoria(1,N,X). % produttoria da 0 a N



% potenza con base X esponente N
potenza(X,1,R):- R is X. 
potenza(X,N,R):- N>1, N1 is N-1, potenza(X,N1,R1), R is X*R1.  

